import pprint

from commandbased import CommandBasedRobot
from hal_impl.data import hal_data
import hal
import wpilib

from commands.groupDriveStraight import GroupDriveStraight
from commands.teleDrive import TeleDrive
from common.oi import oi
from subsystems.driveBase import DriveBase, driveBase

class MyRobot(CommandBasedRobot):
    
    def robotInit(self):
        print("robotInit deadband elimination: {}".format(hal.getPWMEliminateDeadband(driveBase.diabloDrive.frontLeftMotor.handle)))
        self.teleDrive = TeleDrive()
        self.autonomousCommand = GroupDriveStraight()
        # Forced Initializing PWM from hal_data
#         hal_data['pwm'][0]['initialized'] = True
#         hal_data['pwm'][1]['initialized'] = True
#         hal_data['pwm'][2]['initialized'] = True
#         hal_data['pwm'][3]['initialized'] = True
        pprint.pprint(hal_data['pwm'])
    def autonomousInit(self):
        self.autonomousCommand.start()
    def autonomousPeriodic(self):
        pass
    def teleopInit(self):
        self.autonomousCommand.cancel()
        self.teleDrive.start()
    def teleopPeriodic(self):
        oi.backwardsCheck();
    def testInit(self):
        pass
    def testPeriodic(self):
        pass

if __name__ == '__main__':
    wpilib.run(MyRobot)