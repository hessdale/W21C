INSERT INTO w21c.client (username, password, joined_on) VALUES('dale', 'password', now());

INSERT INTO w21c.login (client_id, token) VALUES((select c.id from w21c.client c where c.username = 'dale' and c.password = 'password'), 'randomtoken');
