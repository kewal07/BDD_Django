from aloe import before, step, world
from aloe.tools import guess_types
from aloe_django.steps.models import get_model, reset_sequence
from nose.tools import assert_true, assert_dict_equal, assert_count_equal

from django.contrib.auth.models import User

from rest_framework.test import APIClient

from bdd_customer.models import Transaction

@before.each_feature
def before_each_feature(feature):
    world.client = APIClient()

@step('I empty the "([^"]+)" table')
def step_empty_table(self, model_name):
    model_class = get_model(model_name)
    model_class.objects.all().delete()
    reset_sequence(model_class)

@step('I create the following users:')
def step_create_users(self):
    for user in guess_types(self.hashes):
        User.objects.create_user(**user)

@step('I provide the correct user name "([^"]+)" and the corresponding password "([^"]+)"')
def step_log_in(self, username, password):
    world.is_logged_in = world.client.login(username=username, password=password)

@step('I am successfully logged in')
def step_confirm_log_in(self):
    assert_true(world.is_logged_in)

@step('I create the following transactions:')
def step_create_transactions(self):
	Transaction.objects.bulk_create([
		Transaction(
			user=User.objects.get(id=data['user']),
			amount=data['amount'],
			type_of_transaction=data['type_of_transaction']
		) for data in guess_types(self.hashes)
	])

@step('I get a list of transactions')
def step_get_transactions(self):
    world.response = world.client.get('/transactions')

@step('I see the below response:')
def step_confirm_response_data(self):
    response = world.response.json()
    if isinstance(response, list):
        assert_count_equal(guess_types(self.hashes), response)
    else:
        assert_dict_equal(guess_types(self.hashes)[0], response)

@step('I create the single transaction:')
def step_create_single_transaction(self):
	world.response = world.client.post('/transactions', data=guess_types(self.hashes[0]))