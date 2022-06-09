<script>
  export default {
      name: 'LoginPage'
  };
</script>

<template><form>
  <!-- Login -->
  <div class="form-outline mb-4">
    <input type="login" id="form2Example1" class="form-control" />
    <label class="form-label" for="form2Example1">Login</label>
  </div>

  <!-- Hasło -->
  <div class="form-outline mb-4">
    <input type="password" id="form2Example2" class="form-control" />
    <label class="form-label" for="form2Example2">Password</label>
  </div>

  <!-- Logowanie -->
  <button type="button" class="btn btn-primary btn-block mb-4">Sign in</button>

  <!-- Rejestracja -->
  <div class="text-center">
    <p>Not a member? <a href="/register">Register</a></p>
  </div>
</form></template>
