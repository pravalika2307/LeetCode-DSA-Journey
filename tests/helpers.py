import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def to_linked_list(vals):
    dummy = ListNode(0)
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def from_linked_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def load_solution(rel_path: str):
    path = ROOT / rel_path
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    mod.ListNode = ListNode
    spec.loader.exec_module(mod)
    return mod
