package com.skygreen.SkyGreen.infra.infraSecurity;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Autowired
    private SecurityFilter securityFilter;

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .csrf(csrf -> csrf.disable())  // Desabilita CSRF
                //.cors(cors -> cors.disable())  // Desabilita CORS da forma recomendada
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)) // Define a política de sessão
                .authorizeHttpRequests(auth -> auth                         
                        .requestMatchers(HttpMethod.POST, "/auth/login").permitAll()
                        .requestMatchers(HttpMethod.POST, "/auth/register").hasRole("ADMIN")
                        .requestMatchers( "/usuario/**").hasRole("ADMIN")
                        .requestMatchers( "/compras/**").hasRole("ADMIN")
                        .requestMatchers( "/sementes/**").hasRole("ADMIN")
                        .requestMatchers( "/fornecedor/**").hasRole("ADMIN")
                        .requestMatchers( "/producao/**").hasRole("ADMIN")
                        .requestMatchers( "/estoque/**").hasRole("ADMIN")
                        .requestMatchers( "/prateleira/**").hasRole("ADMIN")
                        .requestMatchers("/usuario/personal/**").authenticated()
                        .requestMatchers("/usuario/**", "/compras/**", "/sementes/**", "/fornecedor/**", "/estoque/**", "/prateleira/**").hasRole("ADMIN")
                        .requestMatchers("/h2-console/**").permitAll()
                        .anyRequest().permitAll()
                )
                .headers(headers -> headers.frameOptions().disable())  // Para permitir o uso do H2
                .addFilterBefore(securityFilter, UsernamePasswordAuthenticationFilter.class);

        return http.build();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration)
            throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
