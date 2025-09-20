import streamlit as st
import pandas as pd
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Streamlit
st.set_page_config(
    page_title="AI Data Chat",
    page_icon="🤖",
    layout="centered"
)

@st.cache_resource
def setup_ai():
    """Initialize Gemini AI model"""
    api_key = os.getenv('GEMINI_API_KEY')
    model_name = os.getenv('GEMINI_MODEL', 'gemini-2.0-flash')
    
    if not api_key:
        return None
    
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def main():
    st.title("🤖 AI Data Chat")
    st.markdown("Upload your data and chat with it using AI!")
    
    # Initialize AI
    ai_model = setup_ai()
    
    if not ai_model:
        st.error("❌ API key not found. Check your .env file.")
        st.info("Make sure your .env file contains: GEMINI_API_KEY=your_key_here")
        return
    
    st.success("✅ AI Ready")
    
    # File upload
    uploaded_file = st.file_uploader(
        "Choose your data file",
        type=['csv', 'xlsx', 'xls'],
        help="Upload a CSV or Excel file to start chatting"
    )
    
    if uploaded_file is not None:
        try:
            # Load data based on file type
            if uploaded_file.name.endswith('.csv'):
                data = pd.read_csv(uploaded_file)
            else:
                data = pd.read_excel(uploaded_file)
            
            # Display data info
            st.success(f"✅ Loaded {len(data):,} rows and {len(data.columns)} columns")
            
            # Data preview
            with st.expander("📊 Data Preview", expanded=True):
                st.dataframe(data.head(5), use_container_width=True)
            
            # Initialize chat history
            if 'messages' not in st.session_state:
                st.session_state.messages = []
            
            # Display chat history
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.write(message["content"])
            
            # Chat input
            if question := st.chat_input("Ask a question about your data..."):
                # Add user message
                st.session_state.messages.append({"role": "user", "content": question})
                
                with st.chat_message("user"):
                    st.write(question)
                
                # Prepare data context for AI
                data_context = f"""
Dataset Information:
- Total rows: {len(data):,}
- Total columns: {len(data.columns)}
- Column names: {list(data.columns)}

Sample data (first 3 rows):
{data.head(3).to_string(index=False)}

Data types:
{data.dtypes.to_string()}
                """
                
                # Create prompt
                prompt = f"""You are a helpful data analyst. Answer the user's question about their dataset.

User Question: {question}

{data_context}

Instructions:
- Answer based only on the data provided
- Be specific and provide exact numbers when possible
- If you need to calculate something, explain your reasoning
- Keep your response clear and helpful

Answer:"""
                
                # Get AI response
                with st.chat_message("assistant"):
                    with st.spinner("Analyzing your data..."):
                        try:
                            response = ai_model.generate_content(prompt)
                            answer = response.text
                            st.write(answer)
                            
                            # Save assistant response
                            st.session_state.messages.append({"role": "assistant", "content": answer})
                            
                        except Exception as e:
                            error_msg = f"Sorry, I encountered an error: {str(e)}"
                            st.error(error_msg)
                            st.session_state.messages.append({"role": "assistant", "content": error_msg})
            
            # Clear chat button
            if st.session_state.messages:
                if st.button("🗑️ Clear Chat History"):
                    st.session_state.messages = []
                    st.rerun()
        
        except Exception as e:
            st.error(f"❌ Error loading file: {str(e)}")
            st.info("Please make sure you uploaded a valid CSV or Excel file.")
    
    else:
        # Instructions when no file is uploaded
        st.info("👆 Upload a CSV or Excel file to get started!")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**📊 What you can ask:**")
            st.markdown("""
            - How many rows/columns?
            - What are the column names?
            - Show me summary statistics
            - What's the average/median/max of [column]?
            - How many unique values in [column]?
            """)
        
        with col2:
            st.markdown("**📁 Supported formats:**")
            st.markdown("""
            - CSV files (.csv)
            - Excel files (.xlsx, .xls)
            - Any size dataset
            - Multiple sheets (Excel)
            """)

if __name__ == "__main__":
    main()
