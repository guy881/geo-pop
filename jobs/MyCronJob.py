from django.core.management import call_command
from django_cron import CronJobBase, Schedule


class MyCronJob(CronJobBase):

    RUN_EVERY_MINS = 60 # every hour

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'jobstemp.PullGDKiAUpdateJob'    # a unique code

    def do(self):
        pass
        call_command('pull_updates_from_GDKiA')