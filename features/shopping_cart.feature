@cart
Feature: Shopping Cart functionality


  Scenario: Add Items to Cart
    Given "STANDARD_USER" is on the Product Listing page
    When the user adds items to cart
      | item_name                |
      | Sauce Labs Backpack      |
      | Sauce Labs Fleece Jacket |
    Then the items should appear in the cart
    And the cart counter should display the expected number of items


  Scenario: Remove Items from Cart
    Given "STANDARD_USER" is on the Product Listing page
    And the user has items in the cart
      | item_name                |
      | Sauce Labs Backpack      |
      | Sauce Labs Fleece Jacket |
      | Sauce Labs Bolt T-Shirt  |
    When the user removes several items
      | item_name                |
      | Sauce Labs Backpack      |
      | Sauce Labs Fleece Jacket |
    Then only not removed items should remain in the cart
    And the cart counter should display the expected number of items