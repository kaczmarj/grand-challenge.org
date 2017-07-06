from comic.celery import debug_task
from evaluation.tasks import add, start_sibling_container


def test_debug_task():
    # Just ensure that the debug task runs
    res = debug_task.delay()
    assert res.state == 'PENDING'
    res.get(timeout=5)
    assert res.state == 'SUCCESS'


def test_add():
    res = add.delay(2, 2)
    assert res.get(timeout=5) == 4


def test_start_sibling_container():
    res = start_sibling_container.delay()
    assert res.get(timeout=10) == 'hello world\n'
