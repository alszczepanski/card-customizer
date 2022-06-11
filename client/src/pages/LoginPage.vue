<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { login } from '@/services/auth';
import { setItem } from '@/services/localstorage';
const formException = ref();
const router = useRouter();
const handleSubmit = (e) => {
  e.preventDefault();
  const formData = new FormData(event.currentTarget)
  const fieldValues = Object.fromEntries(formData.entries())
  const { username, password } = fieldValues;
  if (!username) {
    formException.value = "Nie podano nazwy użytkownika";
    return;
  }
  if (!password) {
    formException.value = "Nie podano hasła";
    return;
  }
  login({ username, password })
    .then(({ data }) => setItem('cards-auth-token', data.access_token))
    .then(() => router.replace("/"))
    .catch(err => formException.value = err.message)
};
</script>

<template>
<form>
 <form @submit="handleSubmit">
    <div class="form-outline mb-4">
      <label class="form-label" for="form2Example1">Login</label>
      <input name="username" type="login" id="form2Example1" class="form-control" />
    </div>

    <div class="form-outline mb-4">
      <label class="form-label" for="form2Example2">Hasło</label>
      <input name="password" type="password" id="form2Example2" class="form-control" />
    </div>


    <button type="submit" class="btn btn-primary btn-block mb-4">Zaloguj się</button>
    <div v-if="formException" class="alert alert-danger" role="alert">
      {{ formException }}
    </div>

    <div class="text-center">
      <p>Nie masz konta? <a href="/register">Zarejestruj się</a></p>
    </div>
  </form>
</template>
