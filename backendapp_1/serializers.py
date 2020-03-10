from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Team, TeamProfile, Problem, Become_Educated, Solution, Action_Blueprint, Impact, BigIssue, RootCause, SolutionPassion, SolutionType

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('name', 'location', 'level','team_logo', 'accepting_members' ,'numMembers')

class TeamProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamProfile
        fields = ('is_complete', 'team')

class ProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Problem
        fields = ('problem', 'team_profile')

class Become_EducatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Become_Educated
        fields = ('become_educated', 'team_profile')

class SolutionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solution
        fields = ('solution', 'team_profile')

class Action_BlueprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action_Blueprint
        fields = ('action_blueprint', 'team_profile')

class ImpactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Impact
        fields = ('name', 'location', 'level','team_logo', 'accepting_members' ,'numMembers')

class BigIssueSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigIssue
        fields = ('big_issue', 'problem','become_educated', 'impact')

class RootCauseSerializer(serializers.ModelSerializer):
    class Meta:
        model = RootCause
        fields = ('title', 'big_issue', 'root_cause')

class SolutionPassionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionPassion
        fields = ('solution', 'solution_passion', 'action_blueprint', 'impact')

class SolutionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolutionType
        fields = ('solution', 'solution_type', 'action_blueprint', 'impact')





