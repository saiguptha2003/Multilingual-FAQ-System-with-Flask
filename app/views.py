import json
from flask import Blueprint, request, jsonify,render_template,redirect,url_for,flash
from .models import FAQ
from app import db
from .cache import redisClient
from .forms import FAQForm
bp = Blueprint('faqsd', __name__, url_prefix='/api/faqs')




@bp.route('/', methods=['GET'])
def get_faqs():
    lang = request.args.get('lang', 'en')
    cache_key = f"faqs_{lang}"
    count_key = f"faqs_count_{lang}"

    try:
        cached_faqs = redisClient.get(cache_key)
        cached_count = redisClient.get(count_key)
        db_count = FAQ.query.count()
        if cached_faqs and cached_count and int(cached_count) == db_count:
            return jsonify(json.loads(cached_faqs))
        faqs = FAQ.query.all()
        faq_list = [faq.translate_faq(lang) for faq in faqs]
        redisClient.set(cache_key, json.dumps(faq_list))
        redisClient.set(count_key, db_count)
        return jsonify(faq_list)
    except Exception as e:
        return jsonify({"error": "Failed to fetch FAQs", "details": str(e)}), 500


@bp.route('/', methods=['POST'])
def add_faq():
    data = request.get_json()
    
    question = data.get('question')
    answer = data.get('answer')
    
    new_faq = FAQ(
        question=question,
        answer=answer
    )
    
    db.session.add(new_faq)
    db.session.commit()
    
    return jsonify({'message': 'FAQ added successfully'}), 201


@bp.route('/add_faq', methods=['GET', 'POST'])
def admin_add_faq():
    form = FAQForm()
    if form.validate_on_submit():
        faq = FAQ(
            question=form.question.data,
            answer=form.answer.data
        )
        db.session.add(faq)
        db.session.commit()
        flash('FAQ added successfully!', 'success')
        return redirect(url_for('faqsd.admin_add_faq'))
    return render_template('create_faq.jinja2', form=form)


@bp.route("/get_faqs_WYSIWYG")
def show_faqs():
    faqs = FAQ.query.all()  
    return render_template("get_faqs.jinja2", faqs=faqs)