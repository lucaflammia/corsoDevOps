Feature: esempio di acceptance test

  Scenario: data un'api rest
     Given build e run del container avviato
      When chiamiamo con una get l'endpoint /
      Then l'api ci saluta correttamente