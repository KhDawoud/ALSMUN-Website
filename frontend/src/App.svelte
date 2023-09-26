<style>
  @import 'tailwindcss/base.css';
  @import 'tailwindcss/components.css';
  @import 'tailwindcss/utilities.css';
</style>

<script lang="ts">
  import LoginForm from "./lib/LoginForm.svelte";
  import LoginBackground from "./assets/LoginBackground.jpg";


</script>

<body class="bg-cover bg-no-repeat bg-center" style="background-image: url('{LoginBackground}');">
  <div class="flex min-h-screen justify-center items-center align-middle">
    <LoginForm />
  </div>
</body>


