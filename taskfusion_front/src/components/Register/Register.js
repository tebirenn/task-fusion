import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import PropTypes from 'prop-types';
import axios from 'axios';
import styles from './Register.module.css';

const Register = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    first_name: '',
    last_name: '',
    password: '',
    password2: '',
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:8000/authe/api/token/user/', formData);
      console.log('Успешная регистрация', response.data);
      navigate('/login');
    } catch (error) {
      console.error('Ошибка при регистрации', error);
    }
  };

  return (
    <div className={styles.Register}>
      <h2>Регистрация</h2>
      <form onSubmit={handleSubmit}>
        <fieldset>
          <label htmlFor="username">Username:</label>
          <input type="text" id="username" name="username" value={formData.username} onChange={handleChange} />
        </fieldset>
        <fieldset>
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" name="email" value={formData.email} onChange={handleChange} />
        </fieldset>
        <fieldset>
          <label htmlFor="first_name">First name:</label>
          <input type="text" id="first_name" name="first_name" value={formData.first_name} onChange={handleChange} />
        </fieldset>
        <fieldset>
          <label htmlFor="last_name">Last name:</label>
          <input type="text" id="last_name" name="last_name" value={formData.last_name} onChange={handleChange} />
        </fieldset>
        <fieldset>
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" name="password" value={formData.password} onChange={handleChange} />
        </fieldset>
        <fieldset>
          <label htmlFor="password2">Password confirm:</label>
          <input type="password" id="password2" name="password2" value={formData.password2} onChange={handleChange} />
        </fieldset>
        <button type="submit">Register</button>
      </form>
    </div>
  );
}

Register.propTypes = {};

Register.defaultProps = {};

export default Register;
