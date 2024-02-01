describe('template spec', () => {
  it('passes', () => {
    cy.visit('/')
    cy.get('.addItem > .material-symbols-outlined').click()
    cy.get('#item_id').type('tester123ID{enter}')
    cy.get('#name').type('tester123Name{enter}')
    cy.get('#quantity-makerspace').type('abc123{enter}')
    cy.get('#quantity-backroom').type('abc456{enter')
    cy.get('#min_amount').type('min69{enter}')
    cy.get('#location').type('urmomshouse{enter}')
    cy.get('#purchase_link').type('uwumommy.com')
    cy.get('#Vendor').select(1)
    cy.get('#Category').select(11)
    cy.get('#image_url').type('https://i.pinimg.com/736x/1b/23/07/1b230783cb0d380a4586f386c4cd7e29.jpg')
    cy.get('.submit-button').click()

  })
})