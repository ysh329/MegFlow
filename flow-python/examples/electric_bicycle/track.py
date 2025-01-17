# MegFlow is Licensed under the Apache License, Version 2.0 (the "License")
#
# Copyright (c) 2019-2021 Megvii Inc. All rights reserved.
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT ARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

#!/usr/bin/env python
# coding=utf-8

from loguru import logger
from megflow import register, Envelope

from warehouse.track_iou import Tracker
import numpy as np


@register(inputs=['inp'], outputs=['out'])
class Track:
    def __init__(self, name, args):
        self.name = name
        self._tracker = Tracker()

    def exec(self):
        envelope = self.inp.recv()
        if envelope is None:
            return

        items = envelope.msg['items']
        # logger.debug(f'track input: {items}')

        tracks, failed_ids = self._tracker.track(items)
        envelope.msg['tracks'] = tracks
        envelope.msg['failed_ids'] = failed_ids
        # logger.debug(f'track output: {tracks},  failed_ids: {failed_ids}')
        self.out.send(envelope)
