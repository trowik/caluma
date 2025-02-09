from django.db import connection
from django.db.migrations.executor import MigrationExecutor
from django.utils import timezone


def migrate_and_get_apps(state):
    executor = MigrationExecutor(connection)
    executor.migrate(state)
    apps = executor.loader.project_state(state).apps
    executor.loader.build_graph()
    return apps


def test_migrate_to_multiple_files(transactional_db):
    app = "caluma_form"
    migrate_from = [(app, "0045_simple_history")]
    migrate_to = [(app, "0046_file_answer_reverse_keys")]

    old_apps = migrate_and_get_apps(migrate_from)

    # Create some old data. Can't use factories here

    Document = old_apps.get_model(app, "Document")
    Form = old_apps.get_model(app, "Form")
    Answer = old_apps.get_model(app, "Answer")
    HistoricalAnswer = old_apps.get_model(app, "HistoricalAnswer")
    HistoricalFile = old_apps.get_model(app, "HistoricalFile")
    File = old_apps.get_model(app, "File")
    Question = old_apps.get_model(app, "Question")
    FormQuestion = old_apps.get_model(app, "FormQuestion")

    the_form = Form.objects.create(slug="main-form")

    file_question = Question.objects.create(type="file", slug="file-question")
    FormQuestion.objects.create(form=the_form, question=file_question)

    doc = Document.objects.create(form=the_form)

    the_file = File.objects.create(name="foo.txt")
    file_ans = Answer.objects.create(
        question=file_question, document=doc, file=the_file
    )
    HistoricalAnswer.objects.create(
        history_date=timezone.now(),
        created_at=timezone.now(),
        modified_at=timezone.now(),
        question=file_question,
        document=doc,
        file=the_file,
    )

    hfile = HistoricalFile.objects.create(
        history_date=timezone.now(),
        created_at=timezone.now(),
        modified_at=timezone.now(),
    )

    hans_without_existing_ans = HistoricalAnswer.objects.create(
        history_date=timezone.now(),
        created_at=timezone.now(),
        modified_at=timezone.now(),
        question=file_question,
        document=doc,
        file_id=hfile.id,
    )

    new_apps = migrate_and_get_apps(migrate_to)

    # Test the new data: `answer.file` should be gone, `answer.files`
    # must contain the old file data
    Answer = new_apps.get_model(app, "Answer")
    HistoricalFile = new_apps.get_model(app, "HistoricalFile")

    file_ans_after = Answer.objects.get(pk=file_ans.pk)

    assert file_ans_after.files.count() == 1
    assert not hasattr(file_ans_after, "file")

    assert HistoricalFile.objects.get(answer_id=hans_without_existing_ans.id)
