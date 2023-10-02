<script lang="ts">
  import { Router, Link, Route } from 'svelte-routing';
  import LoginForm from "./lib/LoginForm.svelte";
  import Home from './lib/Home.svelte';
  import AboutUs from './lib/AboutUs.svelte';
</script>



<Router>
  <Route path="/" component={LoginForm} />
  <Route path='/home' component={Home} />
  <Route path='/about' component={AboutUs} />
</Router>


