import pytest
from ting_file_management.priority_queue import PriorityQueue

high_priority_example = {
        "nome_do_arquivo": "hp_example.txt",
        "qtd_linhas": 18,
        "linhas_do_arquivo": [".", ".", ".", ".", ".", "."],
    }

low_priority_example = {
        "nome_do_arquivo": "lp_example.txt",
        "qtd_linhas": 2,
        "linhas_do_arquivo": [".", "."],
    }


def test_basic_priority_queueing():
    pq = PriorityQueue()

    pq.enqueue(high_priority_example)
    assert len(pq) == 1

    pq.enqueue(low_priority_example)
    assert len(pq) == 2

    assert pq.dequeue() == low_priority_example
    assert len(pq) == 1

    assert pq.dequeue() == high_priority_example
    assert len(pq) == 0

    pq.enqueue(high_priority_example)
    pq.enqueue(low_priority_example)

    assert pq.search(0) == low_priority_example

    with pytest.raises(IndexError):
        pq.search(2) == high_priority_example
