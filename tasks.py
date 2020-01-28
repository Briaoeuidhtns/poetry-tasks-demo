from invoke import task

@task
def build(c):
    c.run('echo Building!')
    c.run('touch built2')
