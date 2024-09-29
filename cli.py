import click
import json_manage
from datetime import datetime
from tabulate import tabulate


current_date = datetime.now().strftime('%Y-%m-%d')

@click.group()
def cli():
    pass

@cli.command()
@click.argument('status', type=str, required=False)
def list(status = None):
    status_list = ['done', 'unstarted', 'in-progress']
    tasks = json_manage.read_json()
    if len(tasks) <= 0:
        print("You don't have any tasks to do")
    else:
        task_table = []
        task_table.append(['ID', 'Description', 'Status', 'CreatedAt', 'UpdateAt'])
        for task in tasks:
            if status is None or task['status'] == status:
                valid_task = [task['id'], task['description'], task['status'], task['created'], task['updated']]
                task_table.append(valid_task)  
        print(tabulate(task_table, headers="firstrow", tablefmt="pipe"))
        

@cli.command()
@click.argument('description', type=str)
@click.pass_context
def add(ctx, description):
    if not description:
        ctx.fail('The description is required')
    else:
        tasks = json_manage.read_json()
        new_id = len(tasks) + 1
        new_task = {
            'id': new_id,
            'description': description,
            'status': 'unstarted',
            'created': current_date,
            'updated': '',
        }
        tasks.append(new_task)
        json_manage.write_json(tasks)
        print(f'New task was created with id {new_id}')


@cli.command()
@click.argument('id', type=int)
@click.pass_context
def delete(id):
    tasks = json_manage.read_json()
    task = next((x for x in tasks if x['id'] == id), None)
    if task is None:
        print(f'Task with id {id} not found')
    else:
        tasks.remove(task)
        json_manage.write_json(tasks)
        print(f'Task with id {id} deleted successfully')


@cli.command()
@click.argument('id', type=int)
@click.option('--description', default=None)
def update(id, description):
    tasks = json_manage.read_json()
    task = next((x for x in tasks if x['id'] == id), None)
    if not task:
        print(f'Task with id {id} not found')
    else:
        if description is not None:
            task['description'] = description
            task['updated'] = current_date
        json_manage.write_json(tasks)
        print(f'Task with {id} has been updated successfully')

@cli.command(name="mark_done")
@click.argument('id', type=int)
def mark_done(id):
    tasks = json_manage.read_json()
    task = next((x for x in tasks if x['id'] == id), None)
    if not task:
        print(f'Task with {id} not found')
    else:
        task['status'] = 'done'
        task['updated'] = current_date
    json_manage.write_json(tasks)
    print(f'Task with id {id} is done, great!')

@cli.command(name="mark_progress")
@click.argument('id', type=int)
def mark_progress(id):
    tasks = json_manage.read_json()
    task = next((x for x in tasks if x['id'] == id), None)
    if not task:
        print(f'Task with {id} not found')
    else:
        task['status'] = 'in-progress'
        task['updated'] = current_date
    json_manage.write_json(tasks)
    print(f'Task with id {id} is in progress, you can finish it!')


if __name__ == '__main__':
    cli()
