
def get_prompt(ticker_list):

    prompt = f"""
    
Provide super concise info about the following stocks. 

If a stock can't be found just ignore it and say nothing. Don't say not found.  

Don't provide citation numbers. Don't use asterisk or dashes.

Don't introduce the list just get to the stocks. 

Say thanks for reading at the end. Something like "Follow me for stock and financial tweets". Change the ending every time. 
        
    """ + ticker_list

    return prompt
