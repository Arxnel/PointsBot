import os

Token = os.getenv('TOKEN')
Prefix = os.getenv('PREFIX', '.')  # The second argument is a default value in case the environment variable is not set
PointsName = os.getenv('POINTS_NAME', 'Goon Tokens')
Log_channel = int(os.getenv('LOG_CHANNEL', '821442828056002602'))
POINTS_TO_BE_GIVEN_PER_MESSAGE = int(os.getenv('POINTS_PER_MESSAGE', '2'))
