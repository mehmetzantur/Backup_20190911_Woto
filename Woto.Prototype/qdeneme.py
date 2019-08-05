# -*- coding: utf-8 -*-
import os, sys, inspect

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from controller.integrationController import IntegrationController


integrationController = IntegrationController()

rows = integrationController.sendWaitingPulse()


# print(rows)
