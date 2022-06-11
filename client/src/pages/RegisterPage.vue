<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { register } from "@/services/auth";
const formException = ref();
const router = useRouter();
const handleSubmit = (e) => {
  e.preventDefault();
  const formData = new FormData(event.currentTarget);
  const fieldValues = Object.fromEntries(formData.entries());
  const { username, password } = fieldValues;
  if (!username) {
    formException.value = "Nie podano nazwy użytkownika";
    return;
  }
  if (!password) {
    formException.value = "Nie podano hasła";
    return;
  }
  register({ username, password })
    .then(() => router.replace("/login"))
    .catch((err) => (formException.value = err.message));
};
</script>

<template>
   <form @submit="handleSubmit">
    <div class="form-outline mb-4">
      <label class="form-label" for="form2Example1">Login</label>
      <input name="username" type="login" id="form2Example1" class="form-control" />
    </div>

    <div class="form-outline mb-4">
      <label class="form-label" for="form2Example2">Hasło</label>
      <input name="password" type="password" id="form2Example2" class="form-control" />
    </div>

    <button type="submit" class="btn btn-primary btn-block mb-4">
      Zarejestruj się
    </button>

    <div class="text-center">
      <p>Masz już konto? <a href="/login">Zaloguj się</a></p>
    </div>
  </form>
</template>