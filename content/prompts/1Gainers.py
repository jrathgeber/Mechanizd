
def get_prompt(ticker_list):

    prompt = f"""
    
Provide super concise info about the following stocks. 

If a stock can't be found just ignore it and say nothing. 

Don't provide citation numbers. 

Don't introduce the list just get to the stocks. 
        
    """ + ticker_list

    return prompt
