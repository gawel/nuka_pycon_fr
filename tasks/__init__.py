# -*- coding: utf-8 -*-
from nuka.task import Task


class mytask(Task):

    def do(self):
        res = self.sh(['ls', '/var'])
        return dict(res, changed=1)

    def diff(self):
        res = self.sh(['ls', '/var'])
        diff=self.texts_diff('', res['stdout'])
        return dict(res, diff=diff)
