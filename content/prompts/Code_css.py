
def get_css_prompt(extra):

    prompt = """
         
Use this CSS styling for and code blocks to give them a pretty appearance.
Asume the file is using this CSS at the begining.

The css should provide:
Dark background similar to popular code editors
Syntax highlighting with colors that match common IDE themes
Proper padding and spacing
Scrollbar for overflow content
Rounded corners and subtle border
Monospace font for better code readability


/* Code block container */
pre {
    background-color: #1e1e1e;
    border-radius: 6px;
    padding: 1rem;
    margin: 1.5rem 0;
    overflow-x: auto;
}

/* Code inside the pre block */
pre code {
    color: #d4d4d4;
    font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
    font-size: 14px;
    line-height: 1.5;
}

/* Syntax highlighting colors */
.keyword {
    color: #569cd6;  /* blue for keywords */
}

.string {
    color: #ce9178;  /* orange for strings */
}

.comment {
    color: #6a9955;  /* green for comments */
}

.function {
    color: #dcdcaa;  /* yellow for functions */
}

.variable {
    color: #9cdcfe;  /* light blue for variables */
}

.number {
    color: #b5cea8;  /* light green for numbers */
}

/* Add some subtle styling for better visibility */
pre {
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
    border: 1px solid #333;
}
Last edited 2 months ago
     
       
    
    """

    return prompt