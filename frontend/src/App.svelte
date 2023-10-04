<script lang="ts">
  import { Router, Route } from 'svelte-routing';
  import LoginForm from "./lib/LoginForm.svelte";
  import Home from './lib/Home.svelte';
  import AboutUs from './lib/AboutUs.svelte';
  import MeetTeam from './lib/MeetTeam.svelte';
  import Secretariat from './lib/Team Pages/Secretariat.svelte';
  import Oc from './lib/Team Pages/OC.svelte';
  import Ac from './lib/Team Pages/AC.svelte';
</script>



<Router>
  <Route path="/" component={LoginForm} />
  <Route path='/home' component={Home} />
  <Route path='/about' component={AboutUs} />
  <Route path='/meet' component={MeetTeam} />
  <Route path='/meet/secretariat' component={Secretariat} />
  <Route path="/meet/oc" component={Oc} />
  <Route path="/meet/ac" component={Ac} />
</Router>


