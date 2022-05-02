import os
import luigi
from automation import automation

logDir:str = os.path.dirname(__file__).replace('\\', '/').replace('/main', '/')
automationLogDir:str = os.path.join(logDir, 'logs/automationLog/')


class LoginEnterCiceron(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def run(self):
        automation.enterLoginCiceron()

class FindFollowDay(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return LoginEnterCiceron()
    def run(self):
        automation.findDayCiceron()

class FindSendHours(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return FindFollowDay()
    def run(self):
        automation.findHoursCiceron()

class FindSendDescription(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return FindSendHours()
    def run(self):
        automation.findDescriptionCiceron()

class FindSendOrientation(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return FindSendDescription()
    def run(self):
        automation.findOrientationCiceron()

class FindSendDifficulties(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return FindSendOrientation()
    def run(self):
        automation.findDifficultiesCiceron()

class FindSendObservations(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return FindSendDifficulties()
    def run(self):
        automation.findObservationsCiceron()

class FindFollowBack(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return FindSendObservations()
    def run(self):
        automation.findBackButton()

class deleteAutomationTempFiles(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return FindFollowBack()
    def run(self):
        automation.tempLoginCiceron(automationLogDir)

if __name__ == '__main__':
    luigi.run()
