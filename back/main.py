from fastapi import FastAPI, HTTPException
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Create the translation pipeline
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast


model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

    # Configure CORS to allow requests from your Vue.js frontend
origins = [
    "http://localhost",           # Add the URL of your Vue.js development server
    "http://localhost:3000",      # Change the port if your Vue.js server is running on a different port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/translate/{text}")
async def translate_text(text: str):
    try:
        # Use the translation pipeline to get the translation
        tokenizer.src_lang = "de_DE"
        encoded_hi = tokenizer(text, return_tensors="pt")
        generated_tokens = model.generate(
            **encoded_hi,
            forced_bos_token_id=tokenizer.lang_code_to_id["en_XX"]
        )
        translation = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
        return {"translation": translation[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))