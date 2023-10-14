# retrieve_utils.py Cheat Sheet

## Module Information

- **Module**: retrieve_utils.py
- **Path**: /home/cplan/dev/The-Digital-Hamlet/plan/autogen/retrieve_utils.py

## Description

The `retrieve_utils.py` module provides utility functions for retrieving and processing text data from various sources.

## Functions

### num_tokens_from_text(text: str, model: str = "gpt-3.5-turbo-0613", return_tokens_per_name_and_message: bool = False) -> Union[int, Tuple[int, int, int]]

- **Description**: Returns the number of tokens used by a text.
- **Parameters**:
  - `text` (str): The text to count tokens from.
  - `model` (str, optional): The language model to use. Defaults to "gpt-3.5-turbo-0613".
  - `return_tokens_per_name_and_message` (bool, optional): Whether to return the number of tokens per name and message. Defaults to False.
- **Returns**: The number of tokens used by the text.

### num_tokens_from_messages(messages: dict, model: str = "gpt-3.5-turbo-0613") -> int

- **Description**: Returns the number of tokens used by a list of messages.
- **Parameters**:
  - `messages` (dict): The list of messages.
  - `model` (str, optional): The language model to use. Defaults to "gpt-3.5-turbo-0613".
- **Returns**: The number of tokens used by the messages.

### split_text_to_chunks(text: str, max_tokens: int = 4000, chunk_mode: str = "multi_lines", must_break_at_empty_line: bool = True, overlap: int = 10) -> List[str]

- **Description**: Splits a long text into chunks of maximum tokens.
- **Parameters**:
  - `text` (str): The text to split into chunks.
  - `max_tokens` (int, optional): The maximum number of tokens per chunk. Defaults to 4000.
  - `chunk_mode` (str, optional): The mode for chunking. Defaults to "multi_lines".
  - `must_break_at_empty_line` (bool, optional): Whether to break at an empty line. Defaults to True.
  - `overlap` (int, optional): The number of overlapping tokens between chunks. Defaults to 10.
- **Returns**: A list of text chunks.

### split_files_to_chunks(files: list, max_tokens: int = 4000, chunk_mode: str = "multi_lines", must_break_at_empty_line: bool = True) -> List[str]

- **Description**: Splits a list of files into chunks of maximum tokens.
- **Parameters**:
  - `files` (list): The list of file paths.
  - `max_tokens` (int, optional): The maximum number of tokens per chunk. Defaults to 4000.
  - `chunk_mode` (str, optional): The mode for chunking. Defaults to "multi_lines".
  - `must_break_at_empty_line` (bool, optional): Whether to break at an empty line. Defaults to True.
- **Returns**: A list of text chunks.

### get_files_from_dir(dir_path: str, types: list = TEXT_FORMATS, recursive: bool = True) -> List[str]

- **Description**: Returns a list of all the files in a given directory.
- **Parameters**:
  - `dir_path` (str): The directory path.
  - `types` (list, optional): The list of file types to include. Defaults to TEXT_FORMATS.
  - `recursive` (bool, optional): Whether to search recursively. Defaults to True.
- **Returns**: A list of file paths.

### get_file_from_url(url: str, save_path: str = None) -> str

- **Description**: Downloads a file from a URL.
- **Parameters**:
  - `url` (str): The URL of the file.
  - `save_path` (str, optional): The path to save the downloaded file. Defaults to None.
- **Returns**: The path of the downloaded file.

### is_url(string: str) -> bool

- **Description**: Returns True if the string is a valid URL.
- **Parameters**:
  - `string` (str): The string to check.
- **Returns**: True if the string is a valid URL, False otherwise.

### create_vector_db_from_dir(
    dir_path: str,
    max_tokens: int = 4000,
    client: API = None,
    db_path: str = "/tmp/chromadb.db",
    collection_name: str = "all-my-documents",
    get_or_create: bool = False,
    chunk_mode: str = "multi_lines",
    must_break_at_empty_line: bool = True,
    embedding_model: str = "all-MiniLM-L6-v2",
)

- **Description**: Creates a vector database from all the files in a given directory.
- **Parameters**:
  - `dir_path` (str): The directory path.
  - `max_tokens` (int, optional): The maximum number of tokens per chunk. Defaults to 4000.
  - `client` (API, optional): The ChromaDB client. Defaults to None.
  - `db_path` (str, optional): The path to the ChromaDB database. Defaults to "/tmp/chromadb.db".
  - `collection_name` (str, optional): The name of the collection. Defaults to "all-my-documents".
  - `get_or_create` (bool, optional): Whether to get or create the collection. Defaults to False.
  - `chunk_mode` (str, optional): The mode for chunking. Defaults to "multi_lines".
  - `must_break_at_empty_line` (bool, optional): Whether to break at an empty line. Defaults to True.
  - `embedding_model` (str, optional): The embedding model to use. Defaults to "all-MiniLM-L6-v2".

### query_vector_db(
    query_texts: List[str],
    n_results: int = 10,
    client: API = None,
    db_path: str = "/tmp/chromadb.db",
    collection_name: str = "all-my-documents",
    search_string: str = "",
    embedding_model: str = "all-MiniLM-L6-v2",
) -> Dict[str, List[str]]

- **Description**: Queries a vector database.
- **Parameters**:
  - `query_texts` (List[str]): The list of query texts.
  - `n_results` (int, optional): The number of results to retrieve. Defaults to 10.
  - `client` (API, optional): The ChromaDB client. Defaults to None.
  - `db_path` (str, optional): The path to the ChromaDB database. Defaults to "/tmp/chromadb.db".
  - `collection_name` (str, optional): The name of the collection. Defaults to "all-my-documents".
  - `search_string` (str, optional): The search string to filter the results. Defaults to "".
  - `embedding_model` (str, optional): The embedding model to use. Defaults to "all-MiniLM-L6-v2".

## Constants

### TEXT_FORMATS

- **Description**: The list of supported text file formats.

## Helper Functions

The `retrieve_utils.py` module also includes several helper functions for working with files and URLs. These functions are used internally and may not be directly called by the user.

