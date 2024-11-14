@checkout
Feature: Checkout functionality

  Background:
  Given "STANDARD_USER" is on the Product Listing page

  Scenario: Checkout Overview Data Correctness
    Given the user has items in the cart
      | item_name                |
      | Sauce Labs Backpack      |
      | Sauce Labs Bike Light    |
    When the user proceeds to the Checkout Overview page
    Then the user should see each item with the correct name, price, and quantity
      | item_name                | item_price | item_qty |
      | Sauce Labs Backpack      | 29.99      | 1        |
      | Sauce Labs Bike Light    | 9.99       | 1        |
    And the total items cost should be the sum of individual item prices
    And the tax should be 8% of the total items cost
    And the billing cost should be the total items cost plus tax

  Scenario: Checkout Completion
    Given the user is on the Checkout Overview page
    When the user submits order
    Then the user should see an order confirmation message
