class BillingAddressException(Exception):
    """
    Raised when address creation fails
    """
    def __init__(self, message, errors=None):
        super(BillingAddressException, self).__init__(f'Failed to get create billing address {message}')

class UnauthenticatedException(Exception):
    """
    Raised when authentication fails from jwt token
    """
    def __init__(self, message, errors=None):
        super(UnauthenticatedException, self).__init__(f'Failed to authenticate user {message}')

class AuthTokenException(Exception):
    """
    Raised when we fail to get an auth token.
    """
    def __init__(self, message, errors=None):
        super(AuthTokenException, self).__init__(f'Failed to get auth token {message}')


class TeamCreateException(Exception):
    """
    Raised when we fail to create a team.
    """
    def __init__(self, message, errors=None):
        super(TeamCreateException, self).__init__(f'Failed to create a team {message}')


class TeamGroupCreateException(Exception):
    """
    Raised when we fail to create a team group.
    """
    def __init__(self, message, errors=None):
        super(TeamGroupCreateException, self).__init__(f'Failed to create a team group {message}')

class LostReasonsCreateException(Exception):
    """
    Raised when we fail to create a lost reason.
    """
    def __init__(self, message, errors=None):
        super(LostReasonsCreateException, self).__init__(f'Failed to create a lost reason {message}')

class UserOrganizationConnetionCreateException(Exception):
    """
    Raised when we fail to create a user to organization connection.
    """
    def __init__(self, message, errors=None):
        super(UserOrganizationConnetionCreateException, self).__init__(f'Failed to create a user organization connection {message}')

class OrganizationCreateException(Exception):
    """
    Raised when we fail to create a organization.
    """
    def __init__(self, message, errors=None):
        super(OrganizationCreateException, self).__init__(f'Failed to create organization defaults {message}')


class OrganizationRenameException(Exception):
    """
    Raised when we fail to rename an organization.
    """
    def __init__(self):
        super(OrganizationRenameException, self).__init__(f'Failed to rename an organization')


class OrganizationUpdateTimezoneException(Exception):
    """
    Raised when we fail to update the timezone for an organization.
    """
    def __init__(self):
        super(OrganizationUpdateTimezoneException, self).__init__(f'Failed to update the timezone of an organization')


class ForwardingPhoneCreateException(Exception):
    """
    Raised when we fail to create a forwarding phone.
    """
    def __init__(self, message, errors=None):
        super(ForwardingPhoneCreateException, self).__init__(f'Failed to create a forwarding phone {message}')


class AgentCreateException(Exception):
    """
    Raised when we fail to create an agent.
    """
    def __init__(self, message, errors=None):
        super(AgentCreateException, self).__init__(f'Failed to create a slingshot agent {message}')

class OrganizationDefaultCreateException(Exception):
    """
    Raised when we fail to create an organization default.
    """
    def __init__(self, message, errors=None):
        super(OrganizationDefaultCreateException, self).__init__(f'Unable to create organization {message}')

class UserSenderCreateException(Exception):
    """
    Raised when we fail to create a user email address.
    """
    def __init__(self, message, errors=None):
        super(UserSenderCreateException, self).__init__(f'Unable to create user email address {message}')

class UserCreateException(Exception):
    """
    Raised when we fail to create a user.
    """
    def __init__(self, message, errors=None):
        super(UserCreateException, self).__init__(f'Unable to create user {message}')


class UserAlreadyExists(Exception):
    """
    A user with this email address already exists
    """
    def __init__(self, message, errors=None):
        super(UserAlreadyExists, self).__init__(f'User with this email already exists {message}')


class UserLookupException(Exception):
    """
    Raised when we fail to lookup a user.
    """
    def __init__(self):
        super(UserLookupException, self).__init__(f'Failed to lookup user')


class InvalidPassword(Exception):
    """
    Password did not meet requirements
    """
    def __init__(self, message, errors=None):
        super(InvalidPassword, self).__init__(f'Password does not meet requirements {message}')


class TaskPhoneCreateException(Exception):
    """
    Raised when we fail to create a task phone.
    """
    def __init__(self, message, errors=None):
        super(TaskPhoneCreateException, self).__init__(f'Unable to create a task phone for user {message}')


class TaskCreateException(Exception):
    """
    Raised when we fail to create a task sequence.
    """
    def __init__(self, message, errors=None):
        super(TaskCreateException, self).__init__(f'Unable to create task sequences for user {message}')


class CodeCreateException(Exception):
    """
    Raised when we fail to create a auth code.
    """
    def __init__(self, message, errors=None):
        super(CodeCreateException, self).__init__(f'Unable to register integration {message}')


class MessageTemplateCreateException(Exception):
    """
    Raised when we fail to create a message template.
    """
    def __init__(self, message, errors=None):
        super(MessageTemplateCreateException, self).__init__(f'Unable to create message templates {message}')


class TaskActionsLookupException(Exception):
    """
    Raised when we fail to list task actions
    """
    def __init__(self, message, errors=None):
        super(TaskActionsLookupException, self).__init__(f'Unable to lookup task actions {message}')


class SlingshotCreateException(Exception):
    """
    Raised when we fail to create a slingshot
    """
    def __init__(self):
        super(SlingshotCreateException, self).__init__(f'Unable to create slingshots')


class CompanyIndustryOptionListException(Exception):
    """
    Raised when we fail to list industry options.
    """
    def __init__(self):
        super(CompanyIndustryOptionListException, self).__init__(f'Unable to list industry options')


class CompanySizeOptionListException(Exception):
    """
    Raised when we fail to list company size options.
    """
    def __init__(self):
        super(CompanySizeOptionListException, self).__init__(f'Unable to list company size options')


class CompanyRoleOptionListException(Exception):
    """
    Raised when we fail to list company role options.
    """
    def __init__(self):
        super(CompanyRoleOptionListException, self).__init__(f'Unable to list company role options')


class CompanyGoalOptionListException(Exception):
    """
    Raised when we fail to list company goal options.
    """
    def __init__(self):
        super(CompanyGoalOptionListException, self).__init__(f'Unable to list company goal options')


class OrganizationProfileCreateException(Exception):
    """
    Raised when we fail to create an organization profile.
    """
    def __init__(self):
        super(OrganizationProfileCreateException, self).__init__(f'Unable to create organization profile')


class SourceCreateException(Exception):
    """
    Raised when we fail to create a source.
    """
    def __init__(self):
        super(SourceCreateException, self).__init__(f'Unable to create a source')
        

class SourceUpdateException(Exception):
    """
    Raised when we fail to update a source.
    """
    def __init__(self):
        super(SourceUpdateException, self).__init__(f'Unable to update a source')

class TeamLookupException(Exception):
    """
    Raised when we fail to lookup a team.
    """
    def __init__(self):
        super(TeamLookupException, self).__init__(f'Unable to lookup team')


class TeamUpdateException(Exception):
    """
    Raised when we fail to update a team.
    """
    def __init__(self):
        super(TeamUpdateException, self).__init__(f'Unable to update team')


class UserTeamAssociationException(Exception):
    """
    Raised when we fail to associate a user to a team.
    """
    def __init__(self):
        super(UserTeamAssociationException, self).__init__(f'Unable to associate a user to a team')
