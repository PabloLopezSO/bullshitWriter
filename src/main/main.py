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

class IterateFillFields(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return LoginEnterCiceron()
    def run(self):
        automation.testIteration()

class DeleteAutomationTempFiles(luigi.Task):
    def output(self):
        return luigi.LocalTarget(f'{automationLogDir}/login.tmp')
    def requires(self):
        return IterateFillFields()
    def run(self):
        automation.tempLoginCiceron(automationLogDir)

if __name__ == '__main__':
    luigi.run()
