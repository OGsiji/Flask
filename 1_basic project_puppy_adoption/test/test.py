import pytest

from sys import path

path.append("/Users/user/Desktop/ML Frameork/Flask/1_basic project_puppy_adoption/")

from adoption_site import app, db, Puppy, Owner

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    with app.app_context():
        db.create_all()
        yield client
        db.drop_all()

def test_index(client):
    response = client.get('/')
    assert b"Welcome to Puppy Adoption" in response.data

def test_add_pup(client):
    response = client.post('/add', data={'name': 'Test Puppy'})
    assert response.status_code == 302  # Redirect status code
    assert Puppy.query.count() == 1  # Check if a puppy was added 

def test_list_pup(client):
    puppy = Puppy(name='Test Puppy')
    db.session.add(puppy)
    db.session.commit()
    response = client.get('/list')
    assert b"Test Puppy" in response.data

def test_add_owner(client):
    puppy = Puppy(name='Test Puppy')
    db.session.add(puppy)
    db.session.commit()
    response = client.post('/add_owner', data={'name': 'Owner 1', 'pup_id': puppy.id})
    assert response.status_code == 302  # Redirect status code
    assert Owner.query.count() == 1  # Check if an owner was added

def test_del_pup(client):
    puppy = Puppy(name='Test Puppy')
    db.session.add(puppy)
    db.session.commit()
    response = client.post('/delete', data={'id': puppy.id})
    assert response.status_code == 302  # Redirect status code
    assert Puppy.query.count() == 0  # Check if the puppy was deleted

if __name__ == '__main__':
    pytest.main()
