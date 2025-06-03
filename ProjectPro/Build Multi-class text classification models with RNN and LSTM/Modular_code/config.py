# ------------------------------------------------------------------------------------------------------------------
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////////    DEFAULT PARAMETERS   ////////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------------------------------------------------------

# Modelling parameters
RANDOM_STATE = 1729
PADDING_LENGTH = 50
LEARNING_RATE = 0.0001
INPUT_SIZE = 50
NUM_EPOCHS = 50
HIDDEN_SIZE = 50

# Important labels
LABEL_COL = "Product"
TEXT_COL = "Consumer complaint narrative"
LABEL_MAP = {
    'Vehicle loan or lease': 'vehicle_loan',
    'Credit reporting, credit repair services, or other personal consumer reports': 'credit_report',
    'Credit card or prepaid card': 'card',
    'Money transfer, virtual currency, or money service': 'money_transfer',
    'virtual currency': 'money_transfer',
    'Mortgage': 'mortgage',
    'Payday loan, title loan, or personal loan': 'loan',
    'Debt collection': 'debt_collection',
    'Checking or savings account': 'savings_account',
    'Credit card': 'card',
    'Bank account or service': 'savings_account',
    'Credit reporting': 'credit_report',
    'Prepaid card': 'card',
    'Payday loan': 'loan',
    'Other financial service': 'others',
    'Virtual currency': 'money_transfer',
    'Student loan': 'loan',
    'Consumer Loan': 'loan',
    'Money transfers': 'money_transfer'
}

# Input
DATA_PATH = "Input/complaints.csv"
GLOVE_VECTOR_PATH = "Input/glove.6B.50d.txt"

# Output
TOKENS_PATH = "Output/tokens{}.pkl"
LABELS_PATH = "Output/labels{}.pkl"
RNN_MODEL_PATH = "Output/model_rnn{}.pth"
LSTM_MODEL_PATH = "Output/model_lstm{}.pth"
VOCABULARY_PATH = "Output/vocabulary{}.pkl"
EMBEDDINGS_PATH = "Output/embeddings{}.pkl"
EMBEDDINGS_V2_PATH = "Output/embeddings_v2{}.pkl"
LABEL_ENCODER_PATH = "Output/label_encoder{}.pkl"
# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------------------------------------------------
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# /////////////////////////////////////////////    EXPERIMENTAL PARAMETERS   ///////////////////////////////////////
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# ------------------------------------------------------------------------------------------------------------------

# INPUT
DATA_S3_PATH = "s3://finbox-data-science/202x/individual/abhishek-bakshi/all_datasets/AccounttypeClassificationData/SMS_for_accounttype_modelling.csv"
S3_ATHENA_FILES = 's3://finboxredshiftdump/datalake/extracted_live/dt={}/move_time={}/{}.parquet'
PRIMARY_CONFIG = {
    'dt': '2024-07-11',
    'move_time': '2024-07-12 11:07:37',
    'filename': '000'
}

PRIMARY_LABEL = 'accounttype'
SECONDARY_LABEL1 = 'smstype'
SECONDARY_LABEL2 = 'sms_tags'
TERTIARY_LABEL1 = 'smssubtype'
TERTIARY_LABEL2 = 'transactiontype'
TERTIARY_LABEL3 = 'transactionchannel'
TEXT_COLUMN = 'smsbody'


# PREPROCESSING
PRIMARY_LABEL_MAP = {}
SECONDARY_LABEL1_MAP = {}
SECONDARY_LABEL2_MAP = {}
TERTIARY_LABEL1_MAP = {}
TERTIARY_LABEL2_MAP = {}
TERTIARY_LABELS3_MAP = {}