# Maklai-Test

## Installation

Instructions on installing the project on your local machine.

1. Clone the repository to your local machine
2. Navigate to the cloned repository directory
3. ```pip install -r requirements.txt```

Now, you should be able to run the application and the tests.

## Usage

1. Run the server with ```uvicorn main:app```
2. Open your browser at ```http://localhost:8000/paraphrase?tree=sometree&limit=somelimit```

### Endpoint Description

```/paraphrase```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;HTTP Method: ```GET```

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Query Parameters:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```tree: str (required)``` - a string representing the syntax tree

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;```limit: int (optional, default: 20)``` - maximum number of paraphrased texts to return
  
### Example

```http://localhost:8000/paraphrase?tree=(S (NP (NP (DT The) (JJ charming) (NNP Gothic) (NNP Quarter) ) (, ,) (CC or) (NP (NNP Barri) (NNP Gòtic) ) ) (, ,) (VP (VBZ has) (NP (NP (JJ narrow) (JJ medieval) (NNS streets) ) (VP (VBN filled) (PP (IN with) (NP (NP (JJ trendy) (NNS bars) ) (, ,) (NP (NNS clubs) ) (CC and) (NP (JJ Catalan) (NNS restaurants) ) ) ) ) ) ) )&limit=20```

In the file ```result.json```, there is there is an example of the result of invoking the endpoint.

## Files

* ```main.py```: The main application file. Contains an endpoint that generates paraphrases of a given syntactic tree
* ```nltk_utils.py```: A helper module containing functions used to process syntax tree
* ```test_main.py```: A unittest file to test the functionality of main.py
* ```test_nltk_utils.py```: A unittest file to test the functionality of nltk_utils.py
* ```README.md```: The file you're currently reading
* ```requirements.txt```: Python packages that project depends on
* ```result.json```: There is an example of the result of invoking the endpoint
