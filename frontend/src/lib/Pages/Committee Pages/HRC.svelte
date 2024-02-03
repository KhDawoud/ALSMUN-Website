
<script lang="ts">
    import NavBar from "../../Components/NavBar.svelte";
    import TopicA from '../../../assets/Committees/HRC/Topic1.jpg';
    import TopicB from '../../../assets/Committees/HRC/Topic2.jpg';
    import InfoText from "../../Components/InfoText.svelte";
  
  
  </script>
  
  <NavBar />

<h1 class="text-center font-bold underline text-6xl my-10"> Human Rights Council </h1>
  <div class="grid grid-flow-row mx-auto space-y-8">
  <InfoText 
    image={TopicA}
    title="Topic 1: The Darfur Genocide and Humanitarian Aid "
    paragraphB=""
    paragraphA="The Darfur genocide, which unfolded in the early 2000s in western Sudan, is marked by
    widespread violence, mass atrocities, and systematic human rights abuses. This conflict was a result of
    long-standing tensions over resources, the conflict involved the Sudanese government and
    government backed-militias, notably the Janjaweed, clashing with rebel groups that represent
    maraginalised communities. The significance of the Darfur genocide lies in its devastating
    humanitarian effects, resulting in hundreds of thousands killed and millions displaced. The
    international community’s response showcased both the challenges of intervening in such crises and
    the debates over whether the events constituted genocide."
    link="https://drive.google.com/file/d/18WcLL2SwVcrIn215fVcZgJES5qo9Jf7-/view?usp=sharing"
    />

  <InfoText 
    image={TopicB} 
    title="Topic 2: Transgender People: Civil Rights"
    paragraphB=""
    paragraphA="The issue at hand pertains to the civil rights of transgender individuals and the pressing need
    to address and decrease discrimination against them. Transgender people face significant challenges
    in various aspects of their lives, including healthcare, employment, education, and everyday
    interactions. Discrimination based on gender identity undermines their fundamental rights and
    hinders their ability to live authentically and without fear of prejudice or mistreatment."
    link="https://drive.google.com/file/d/1MRPMCOC9vPJRfPXQDvpHmb4BNij4OvE1/view?usp=sharing"
    />
</div>

