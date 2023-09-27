<script lang="ts">
  import { Router, Link, Route } from 'svelte-routing';
  import LoginForm from "./lib/LoginForm.svelte";
  import Home from './lib/Home.svelte';
</script>



<Router>
  <Route path="/" component={LoginForm} />
  <Route path='/home' component={Home} />
</Router>


