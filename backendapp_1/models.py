from django.db import models
from django.utils.translation import gettext_lazy as _

class Team(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30) #how to make this a 1-1? Preset selection of schools? Coordinates?
    level = models.IntegerField()
    team_logo = models.FileField()
    accepting_members = models.BooleanField(default=True)
    numMembers = models.IntegerField(default=0)
    # mentor = models.OneToOneField(Mentor, on_delete=models.CASCADE)
    # objects = models.Manager


    class Meta:
        permissions = (
            ('create_team', 'Create a Team'),
            ('join_team', 'Join Team')
        )

    # def get_absolute_url(self): #return details page (benchmarks) of team created
    #     return reverse('TeamMap:detail', kwargs={'pk': self.pk}) #pass in with pk, hidden in class Team
    #     #use pk of whatever team just created(viewed?)


    def __str__(self):
        return "{}".format(self.name, self.accepting_members)

    # each is column
    # each album has ID numer, goes up by 1 for each new
    # unique key = ID number


class TeamProfile(models.Model):
    # team = models.ForeignKey(Team, )
    # problem = models.OneToOneField(Problem, on_delete=models.CASCADE)
    # become_educated = models.OneToOneField(Become_Educated, on_delete=models.CASCADE)
    # solution = models.OneToOneField(Solution, on_delete=models.CASCADE)
    # action_blueprint = models.OneToOneField(Action_Blueprint, on_delete=models.CASCADE)
    # impact = models.OneToOneField(Impact, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default=False)
    team = models.ForeignKey(Team, verbose_name="Team", on_delete=models.CASCADE)

class Problem(models.Model):
    problem = models.CharField(max_length=30)
    team_profile = models.ForeignKey(TeamProfile, on_delete = models.CASCADE)
    # big_issue = models.ManyToManyField(BigIssue, on_delete = models.CASCADE) #Many big issues can relate to one problem

class Become_Educated(models.Model):
    become_educated = models.FileField()
    team_profile = models.ForeignKey(TeamProfile, on_delete=models.CASCADE)
    # big_issue = models.ManyToManyField(BigIssue, on_delete=models.CASCADE)

class Solution(models.Model):
    solution = models.CharField(max_length=30)
    team_profile = models.ForeignKey(TeamProfile, on_delete=models.CASCADE)
    # solution_type = models.OneToOneField(SolutionType, on_delete=models.CASCADE)
    # solution_passions = models.ManyToManyField(SolutionPassion, on_delete=models.CASCADE)

class Action_Blueprint(models.Model):
    action_blueprint = models.FileField()
    team_profile = models.ForeignKey(TeamProfile, on_delete=models.CASCADE)
    # solution_type = models.OneToOneField(SolutionType, on_delete=models.CASCADE)
    # solution_passions = models.ManyToManyField(SolutionPassion, on_delete=models.CASCADE)

class Impact(models.Model):
    impact = models.FileField()
    team_profile = models.ForeignKey(TeamProfile, on_delete=models.CASCADE)
    # big_issue = models.ManyToManyField(BigIssue, on_delete=models.CASCADE)
    # solution_type = models.OneToOneField(SolutionType, on_delete=models.CASCADE)
    # solution_passions = models.ManyToManyField(SolutionPassions, on_delete=models.CASCADE)

class BigIssue(models.Model):
        BIG_ISSUE = (
            (1, _('Poverty')),
            (2, _('Hunger')),
            (3, _('Health')),
            (4, _('Education')),
            (5, _('Gender Equality')),
            (6, _('Refugees')),
            (7, _('Water')),
            (8, _('Energy')),
            (9, _('Labor')),
            (10, _('Inequality')),
            (11, _('Sustainability')),
            (12, _('Consumption')),
            (13, _('Climate')),
            (14, _('Conservation')),
            (15, _('Conflict')),
        )

        big_issue = models.PositiveSmallIntegerField(choices=BIG_ISSUE, default=1)
        problem = models.ForeignKey(Problem, on_delete = models.CASCADE)
        become_educated = models.ForeignKey(Become_Educated, on_delete=models.CASCADE)
        impact = models.ForeignKey(Impact, on_delete=models.CASCADE)
        # root_cause = models.ManyToManyField(RootCause, on_delete=models.CASCADE)  # can have more than one root cause

class RootCause(models.Model):

    title = models.CharField(max_length=30) #title is unique - can reuse root causes which build as people add them
    big_issue = models.ForeignKey(BigIssue, on_delete= models.CASCADE )
    #can add root cause yourself or use one smallworld has premade
    root_cause = models.ForeignKey('self', on_delete = models.CASCADE)


class SolutionPassion(models.Model):
    SOLUTION_PASSION = (
        (1, _('Music')),
        (2, _('Art')),
        (3, _('Sports')),
        (4, _('Coding')),
        (5, _('Baking')),
        (6, _('Speaking'))
    )

    solution_passion = models.PositiveSmallIntegerField(choices=SOLUTION_PASSION, default=1)
    solution = models.ForeignKey(Solution, on_delete = models.CASCADE)
    action_blueprint = models.ForeignKey(Action_Blueprint, on_delete=models.CASCADE)
    impact = models.ForeignKey(Impact, on_delete=models.CASCADE)


class SolutionType(models.Model):

    SOLUTION_TYPE = (
        (1, _('Community Objective')),
        (2, _('Fundraising')),
        (3, _('Awareness & Analysis'))
    )

    solution_type = models.PositiveSmallIntegerField(choices=SOLUTION_TYPE, default=1)
    solution = models.ForeignKey(Solution, on_delete=models.CASCADE)
    action_blueprint = models.ForeignKey(Action_Blueprint, on_delete=models.CASCADE)
    impact = models.ForeignKey(Impact, on_delete=models.CASCADE)



