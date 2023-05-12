import os

from fastapi import FastAPI, File, UploadFile, HTTPException, Form, Response, status

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def listModels():
    return ['all-MiniLM-L6-v2',
            'average_word_embeddings_komninos',
            'multi-qa-MiniLM-L6-cos-v1',
            'bert-base-nli-mean-tokens',
            'all_datasets_v3_mpnet-base',
            'paraphrase-MiniLM-L6-v2',
            'all-mpnet-base-v2',
            'average_word_embeddings_glove.6B.300d']