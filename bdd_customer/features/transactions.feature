Feature: Customer transactions
	
	Scenario: Login the user

		Given I empty the "User" table
		
		And I create the following users:
		| id | username | password |
		| 1  | john_doe | password |	
		
		When I provide the correct user name "john_doe" and the corresponding password "password"
		
		Then I am successfully logged in

	Scenario: A customer with no transactions sees an empty list

		Given I empty the "Transaction" table

		When I get a list of transactions

		Then I see the below response:
		| id | amount | type_of_transaction |

	Scenario: A customer with a single transactions sees one item in the  list

		Given I empty the "Transaction" table

		And I create the single transaction:
		| user | amount | type_of_transaction |
		| 1    | 100	| CRE			      |

		When I get a list of transactions

		Then I see the below response:
		| id | amount | type_of_transaction |