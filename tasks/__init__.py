# -*- coding: utf-8 -*-
from nuka.task import Task


class mytask(Task):

    def do(self):
        res = self.sh(['ls', '/etc'])
        return res
