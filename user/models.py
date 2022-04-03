from flask import Flask, jsonify, request, session, redirect
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class User:

    def start_session(self, user):
        """
        Function to start a new session when user is loggin in
        :param user: user object
        :return: user object with code 200 (successful session creation)
        """
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self):
        """
        function to create a new user.
        Encrypt Password using hash function.

        """
        print(request.form)

        # Create the user object
        user = {
            "_id": uuid.uuid4().hex,
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }

        # Encrypt the password
        user['password'] = pbkdf2_sha256.encrypt(user['password'])

        # Check for existing email address
        if db.users.find_one({"email": user['email']}):
            return jsonify({"error": "Email address already in use"}), 400

        if db.users.insert_one(user):
            return self.start_session(user)

        return jsonify({"error": "Signup failed"}), 400

    def signout(self):
        """
        Function to Signout and clear the session
        :return: redirect the user to home page.
        """
        session.clear()
        return redirect('/')

    def login(self):
        """
        Function to login
        :return: new session with user details
        """
        user = db.users.find_one({
            "email": request.form.get('email')
        })

        # Check if user email exist and password in the form and encrypted password from db are same
        if user and pbkdf2_sha256.verify(request.form.get('password'), user['password']):
            return self.start_session(user)

        return jsonify({ "error": "Invalid login credentials"}), 401