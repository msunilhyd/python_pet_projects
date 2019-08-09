from jira import JIRA
import requests

class JiraException(Exception):
    pass

class Jira(object):
    __options = {
        'server':'your server url',
        'verify':False
    }

    __client = None
    def __init__(self, **kwargs):
        self.__client = JIRA('your server url',basic_auth=("username", "password"))
            

    def getProjects(self, raw=False):
        Projects = []
        for project in self.__client.projects():
            if raw:
                Projects.append(project)
            else:
                Projects.append({'Name':project.key, 'Description':project.name})
            return Projects

    def getIssues(self, maxResults=10, raw=False, **kwargs):
        Issues = []
        if len(kwargs) < 1:
            raise JiraException('You need to specify a search criteria')
        else:
            searchstring = ' '.join([( _ + "=" + kwargs[_]) if _ != 'condition' else kwargs[_] for _ in kwargs])
            for item in self.__client.search_issues(searchstring, maxResults = maxResults):
                if raw:
                    Issues.append(item)
                else:
                    Issues.append({'Assignee':item.fields.assignee,'TimeSpent':item.fields.timespent,'CreateDate':item.fields.created,'DueDate':item.fields.duedate,'ResolutionDate':item.fields.resolutiondate,'Status':item.fields.status,'Peer Reviewer':item.fields.customfield_13307,'Reporter':item.fields.reporter,'Name':str(item), 'Summary':item.fields.summary, 'Description':item.fields.description})
        return Issues


if __name__ == '__main__':
    MyJira = Jira()
    print(MyJira.getProjects())
    print(MyJira.getIssues('Beta to GA migration - UEM 3.96 - QA'))


