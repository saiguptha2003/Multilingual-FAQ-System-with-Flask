import boto3
import json
translate = boto3.client(service_name='translate', use_ssl=True)

def lambda_handler(event, context):
    try:
        text_to_translate_question = event.get('question', None)
        text_to_translate_answer= event.get('answer', None)
        target_language = event.get('target_language', None)
        result_question = translate.translate_text(
            Text=text_to_translate_question, 
            SourceLanguageCode="auto",  
            TargetLanguageCode=target_language
        )
        result_answer = translate.translate_text(
            Text=text_to_translate_answer,
            SourceLanguageCode="auto", 
            TargetLanguageCode=target_language
        )
        return {
            "statusCode": 200,
            "body": json.dumps({
                "translated_text_question": result_question,
                "translated_text_answer": result_answer,
                "target_language": target_language
            })
        }
    
    except Exception as e:
        print(f"Error during translation: {str(e)}")
        return {
            "statusCode": 500,
            "body": f"Error: {str(e)}"
        }
