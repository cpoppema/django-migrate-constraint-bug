This project is a test to show issues during `python manage.py migrate` when changing the field type for a field with a constraint.

Related tickets: [28305](https://code.djangoproject.com/ticket/28305), [30152](https://code.djangoproject.com/ticket/30152).

It seems 28305 does not fix this specific problem since the same error message can still occur. 30152 seems to fix the `related_name='+'` issue and we then end up with an exception:

```
django.db.utils.IntegrityError: (1215, 'Cannot add foreign key constraint')
```

Why does this happen ? The two tables have incompatible types for the same field. MySQL (tested on 5.7) needs to have to same type for both fields to be able to add a constraint.

## How to test the bug

The bug is demonstrated by running the test suite. This will attempt to create a test db by running the migrations and should fail in git branches `cannot-add-foreign-key-constraint` and `cannot-change-column-used-in-a-foreign-key-constraint`. The error doesn't happen in master

Make sure you have a MySQL server installed and edit the settings in `myproject/myproject/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test',
        'USER': 'test',
        'PASSWORD': 'test',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET default_storage_engine=InnoDB',
        },
    }
}
```

Then install tox and run `tox` to run the test.
