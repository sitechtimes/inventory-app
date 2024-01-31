describe('template spec', () => {
  it('passes', () => {
    cy.visit('/')
    cy.get('.addItem > .material-symbols-outlined').click()
    cy.get('#item_id').type('tester123ID{enter}')
    cy.get('#name').type('tester123Name{enter}')
    cy.get('#quantity-makerspace').type('abc123{enter}')
    cy.get('#quantity-backroom').type('456{enter')
  })
})