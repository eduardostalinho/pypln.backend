# coding: utf-8
#
# Copyright 2015 NAMD-EMAP-FGV
#
# This file is part of PyPLN. You can get more information at: http://pypln.org/.
#
# PyPLN is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyPLN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyPLN.  If not, see <http://www.gnu.org/licenses/>.

from celery import Celery
from kombu import Exchange, Queue
import config

app = Celery('pypln_workers', backend='mongodb',
        broker='amqp://', include=['pypln.backend.workers'])
app.conf.update(
    BROKER_URL=config.BROKER_URL,
    CELERY_RESULT_BACKEND=config.CELERY_RESULT_BACKEND,
    CELERY_QUEUES=(Queue(config.CELERY_QUEUE_NAME,
        Exchange(config.CELERY_QUEUE_NAME),
            routing_key=config.CELERY_QUEUE_NAME),),
    CELERY_DEFAULT_QUEUE=config.CELERY_DEFAULT_QUEUE,
)
