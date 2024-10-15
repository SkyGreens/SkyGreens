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

import com.skygreen.SkyGreen.Util.JwtUtil;

@Configuration
@EnableWebSecurity
public class SecurityConfiguration {

    @Autowired
    private SecurityFilter securityFilter;

    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception {
        http
                .csrf(csrf -> csrf.disable()) 
                //.cors(cors -> cors.disable())  // Desabilita CORS da forma recomendada
                .sessionManagement(session -> session.sessionCreationPolicy(SessionCreationPolicy.STATELESS)) 
                .authorizeHttpRequests(auth -> auth                         
                        .requestMatchers(JwtUtil.ENDPOINTS_WITH_USER_CAN_ACCESS).permitAll()
                        .requestMatchers(JwtUtil.ENDPOINTS_WITH_ADMIN_CAN_ACCESS).hasRole("ADMIN")
                        .requestMatchers(HttpMethod.GET, JwtUtil.ENDPOINTS_WITH_ASSISTENTE_CAN_ACCESS).hasAnyRole("ADMIN","ASSISTENTEPRODUCAO", "GERENTEPRODUCAO")
                        .requestMatchers(JwtUtil.ENDPOINTS_WITH_GERENTE_CAN_ACCESS).hasAnyRole("ADMIN","GERENTEPRODUCAO")
                        .requestMatchers("/h2-console/**").permitAll()
                        .anyRequest().authenticated()
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
